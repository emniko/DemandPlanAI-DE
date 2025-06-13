import geopandas as gpd
import numpy as np
from scipy.spatial.distance import cdist

hospitals = gpd.read_file("hospitals.shp")  # Supply points (with 'beds' column)
population = gpd.read_file("population.shp")  # Demand points (with 'pop' column)

# Step 1: Define catchments and decay function
CATCHMENT_RADIUS = 30_000  # 30 km (adjust as needed)
DECAY_FUNCTION = "gaussian"  # Options: "gaussian", "exponential", "linear"

def distance_decay(d, radius, method="gaussian"):
    """Calculate distance decay weights."""
    if method == "gaussian":
        return np.exp(-0.5 * (d / radius) ** 2)
    elif method == "exponential":
        return np.exp(-d / radius)
    elif method == "linear":
        return np.maximum(1 - d / radius, 0)
    else:
        raise ValueError("Invalid decay function")
    
    
def compute_iFCA_accessibility(population_gdf, hospitals_gdf, radius=30000, decay_method="gaussian", beds_column="beds"):
    """
    Compute iFCA accessibility given hospital and population GeoDataFrames.
    
    Parameters:
        population_gdf: GeoDataFrame with population points and 'pop' column
        hospitals_gdf: GeoDataFrame with hospital points and 'beds' column (or custom)
        radius: Catchment radius in meters
        decay_method: 'gaussian', 'exponential', or 'linear'
        beds_column: column in hospitals_gdf to use for supply (can be modified by RL)
    
    Returns:
        accessibility_scores: np.array of accessibility values for each population point
    """
    coords_hosp = np.array(list(zip(hospitals_gdf.geometry.x, hospitals_gdf.geometry.y)))
    coords_pop = np.array(list(zip(population_gdf.geometry.x, population_gdf.geometry.y)))
    distances = cdist(coords_pop, coords_hosp, 'euclidean')  # Shape: (n_pop, n_hosp)

    accessibility = np.zeros(len(population_gdf))

    for i in range(len(population_gdf)):
        for j in range(len(hospitals_gdf)):
            if distances[i, j] <= radius:
                D_i = population_gdf.iloc[i]['pop']
                catchment_j = distances[:, j] <= radius
                total_demand_j = population_gdf[catchment_j]['pop'].sum()
                S_j = hospitals_gdf.iloc[j][beds_column]
                weight = distance_decay(distances[i, j], radius, method=decay_method)
                accessibility[i] += (S_j * weight) / (total_demand_j + 1e-9)

    return accessibility
