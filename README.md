# Agentic AI for Hospital prediction

This repository contains 2 Jupyter Notebooks (`DQN.ipynb` and `DQN_iFCA.ipynb`) which contains the main code for the two different experiments we conducted using two distinct reward functions. The first one tries to calculate the correct department which needs more allocation based on patient demand and penalizes over utilization through loss:
```bash
total_reward = (
        0.7 * balance_reward +    
        0.3 * diagnostic_reward -           
        overcrowding_penalty      
   )
```
Similarly the second notebook calculates the mean iFCA and we try to maximize it by giving positive rewards for a better score. The reward function is defined as : 
```bash
total_reward = current_mean - previous_mean
```   

## Installation

Clone this repository and install requirements:
   ```bash
   git clone https://github.com/emniko/DemandPlanAI-DE.git
   cd DemandPlanAI-DE
   pip install -r requirements.txt
