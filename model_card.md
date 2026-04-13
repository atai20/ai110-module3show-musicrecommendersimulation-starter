# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatcher 1.0  

---

## 2. Intended Use  

This recommender generates personalized music recommendations based on user preferences for genre, mood, energy level, and acoustic preference. It's designed for classroom exploration to understand how content-based filtering works, not for real production use. It assumes users have clear preferences for these attributes and that songs can be matched directly to them.

---

## 3. How the Model Works  

The system scores songs by matching user preferences: +2 points for genre match, +1 for mood match, energy similarity (closer values get higher scores, doubled in weight), and +0.5 if the user likes acoustic and the song is acoustic. It then ranks songs by total score and returns the top ones with reasons.

Features used: genre, mood, energy (0-1 scale), acousticness. User considers favorite_genre, favorite_mood, target_energy, likes_acoustic.

From starter, I added energy similarity scoring and acoustic bonus.

---

## 4. Data  

20 songs in the catalog, expanded from 10 with diverse genres (pop, lofi, rock, electronic, folk, jazz, ambient, synthwave, indie, blues, reggae, country) and moods (happy, chill, intense, relaxed, moody, focused, energetic, calm, aggressive, smooth, peaceful, party, sad, heartfelt). Added numerical features like valence, danceability, acousticness. Missing: user listening history, collaborative data, tempo matching beyond energy.

---

## 5. Strengths  

Works well for users with strong genre preferences, as genre match gives high points. Captures energy vibe well with the similarity score. For chill lofi fans, it prioritizes low-energy, acoustic songs accurately.

---

## 6. Limitations and Bias 

Over-prioritizes genre (2 points) over mood (1), so might recommend wrong mood if genre matches. Energy weight doubled might make it too sensitive to energy, ignoring other factors. Underrepresents some genres like country or reggae. Acoustic bonus only applies if explicitly set, missing nuanced acoustic preferences. May create filter bubbles by always favoring matching genres.

---

## 7. Evaluation  

Tested with three profiles: High-Energy Pop (pop, happy, 0.9 energy), Chill Lofi (lofi, chill, 0.4, acoustic), Deep Intense Rock (rock, intense, 0.95). Looked for top songs matching preferences. Surprised that energy similarity became dominant after doubling weight. Ran experiment doubling energy weight, which shifted rankings toward energy matches.

---

## 8. Future Work  

Add more features like valence for positivity, danceability. Improve explanations with more details. Add diversity penalty to avoid too many same artists/genres. Handle multiple preferences or ranges instead of exact matches. Incorporate collaborative filtering with user history.

---

## Personal Reflection

Biggest learning: How simple weighted scoring can simulate recommendations, but biases emerge easily. AI tools helped generate diverse songs and brainstorm scoring rules, but I double-checked math. Surprised that doubling energy weight made rankings more energy-focused, showing sensitivity. Next, I'd add user feedback loop or more features like tempo.  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
