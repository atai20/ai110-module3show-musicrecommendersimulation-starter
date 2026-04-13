# Reflection on Music Recommender Evaluation

## Profile Comparisons

### High-Energy Pop vs Chill Lofi
High-energy pop profile (pop, happy, 0.9 energy) recommends energetic pop songs like Dance Fever and Gym Hero with high danceability and energy. Chill lofi profile (lofi, chill, 0.4 energy, acoustic) shifts to low-energy acoustic tracks like Midnight Coding and Library Rain. This makes sense because the energy preference (0.9 vs 0.4) drives the biggest difference, with chill profile also benefiting from acoustic bonus.

### High-Energy Pop vs Deep Intense Rock
Both profiles have high energy (0.9 vs 0.95), but pop profile favors pop genre with happy mood, recommending Sunrise City and Dance Fever. Rock profile favors rock with intense mood, recommending Storm Runner and Thunder Clap. The genre match (2 points) dominates over slight energy difference, showing how genre weighting creates different recommendations even with similar energy.

### Chill Lofi vs Deep Intense Rock
Chill lofi (low energy, acoustic) recommends calm acoustic lofi like Midnight Coding. Deep intense rock (high energy, rock) recommends aggressive high-energy rock like Storm Runner. The energy difference (0.4 vs 0.95) and genre (lofi vs rock) create completely different vibes, validating that the system captures distinct musical preferences.

These comparisons show the system effectively differentiates based on user preferences, with energy being highly influential after doubling its weight.