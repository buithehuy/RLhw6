# Tic-Tac-Toe with Q-Learning
In this repository, we train agents to play 4x4 and 5x5 Tic-Tac-Toe games using Q-Learning.

## How It Works
The agents are trained by a teacher agent that knows the optimal strategy but only follows this strategy with a given probability `p`. At each turn, the teacher either:

- Chooses the optimal move (with probability `p`)
- Chooses a random valid move (with probability `1 - p`)

This random behavior allows the learning agents to occasionally win and learn from their successes.

To initialize the Q-values for the learning agent, we use Python's `defaultdict` with default values of 0, meaning that every state-action pair starts with a Q-value of 0.

### Q-Learner Class
Implements the Q-Learning algorithm, where Q-values are updated using the following formula:
Q(s_t, a_t) = Q(s_t, a_t) + α * [r_{t+1} + γ * max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t)]
Where:
- `s_t` is the current state,
- `a_t` is the action taken at time `t`,
- `α` is the learning rate,
- `r_{t+1}` is the reward received after taking action `a_t`,
- `γ` is the discount factor,
- `s_{t+1}` is the next state after action `a_t`,
- `max_{a'}` is the highest Q-value for the next state-action pair.

## Code Structure
### `teacher.py`
Implements the Teacher Agent, which knows the optimal policy for any given state. However, the teacher follows this policy only with a set probability.

### `agent.py`
Implements the Q-Learning Agents, which learn based on their interactions with the environment (the game board).

### `game.py`
Contains the main `Game` class, which handles the game logic and state management. The primary game loop is found in the `playGame()` method.

## Running the Program
### 1. Train a New Agent with Teacher Guidance
To train a new RL agent with the help of a teacher agent, use the `-t` flag followed by the number of game iterations you want to train:

```bash
python play.py -a q -t 5000

### 2. Load a Trained Agent and View Reward History
To load a pre-trained agent and view a plot of its cumulative reward history, run the following script:

```bash
python plot_agent_reward.py -p q_agent.pkl
```
## Result
The reward plot illustrates how the agent learns and improves its strategy as it plays more games. In each episode, if agent wins reward += 1, draws = 0 and -= 1 if lose
10000 games played with 4x4 board:
![Figure_1](https://github.com/user-attachments/assets/44799a93-2b73-4cdb-b1b8-99c85f6edb35)
300000 games played with 5x5 board:
![Figure_2](https://github.com/user-attachments/assets/094b8b7f-2e78-467b-af0e-fd73eb1f1584)

