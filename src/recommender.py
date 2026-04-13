from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Score each song
        scored = []
        for song in self.songs:
            score = self._score_song(user, song)
            scored.append((song, score))
        # Sort by score desc
        scored.sort(key=lambda x: x[1], reverse=True)
        return [s[0] for s in scored[:k]]

    def _score_song(self, user: UserProfile, song: Song) -> float:
        score = 0.0
        if song.genre == user.favorite_genre:
            score += 2.0
        if song.mood == user.favorite_mood:
            score += 1.0
        energy_diff = abs(song.energy - user.target_energy)
        energy_score = (1 - energy_diff) * 2  # doubled
        score += energy_score
        if user.likes_acoustic and song.acousticness > 0.5:
            score += 0.5
        return score

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append("genre match")
        if song.mood == user.favorite_mood:
            reasons.append("mood match")
        energy_diff = abs(song.energy - user.target_energy)
        energy_score = (1 - energy_diff) * 2
        reasons.append(f"energy similarity {energy_score:.2f}")
        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append("acoustic preference")
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': int(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []
    
    # Genre match: +2
    if song['genre'] == user_prefs.get('genre'):
        score += 2.0
        reasons.append("genre match (+2.0)")
    
    # Mood match: +1
    if song['mood'] == user_prefs.get('mood'):
        score += 1.0
        reasons.append("mood match (+1.0)")
    
    # Energy similarity: 1 - abs(diff), scaled to 0-1, then *2
    energy_diff = abs(song['energy'] - user_prefs.get('energy', 0.5))
    energy_score = (1 - energy_diff) * 2
    score += energy_score
    reasons.append(f"energy similarity ({energy_score:.2f})")
    
    # Acoustic bonus: if likes_acoustic and acousticness > 0.5, +0.5
    if user_prefs.get('likes_acoustic', False) and song['acousticness'] > 0.5:
        score += 0.5
        reasons.append("acoustic preference (+0.5)")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))
    
    # Sort by score descending
    scored.sort(key=lambda x: x[1], reverse=True)
    
    return scored[:k]
