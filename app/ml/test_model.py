import pickle
import pandas as pd

# --- Step 1: Define the Recommendation Function ---
def get_content_based_recommendations(title, cosine_sim, df, indices, n=10):
    try:
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:n+1]
        game_indices = [i[0] for i in sim_scores]
        return df['title'].iloc[game_indices]
    except KeyError:
        return f"Error: Title '{title}' not found in the dataset."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Step 2: Load Your Saved Data Dictionary ---
MODEL_PATH = 'game_recommender-model.pkl'
print(f"Loading model and data from '{MODEL_PATH}'...")

try:
    with open(MODEL_PATH, 'rb') as f:
        loaded_data = pickle.load(f)
    
    # Access the items from the dictionary by their keys.
    
    print("\n--- Inspecting Dictionary Keys ---")
    print(f"Keys found in loaded dictionary: {list(loaded_data.keys())}")
    
    cosine_sim_matrix = loaded_data['similarity_matrix']
    df_clean = loaded_data['df']
    indices = loaded_data['indices']

    # ----------------------

    print("\nModel and data unpacked successfully from dictionary!")
    print(f"Dataset contains {len(df_clean)} items.")

except FileNotFoundError:
    print(f"\nError: The file '{MODEL_PATH}' was not found.")
    exit()
except KeyError as e:
    print(f"\nFATAL ERROR: A required key was not found in the dictionary: {e}")
    print("Please make sure you are using the correct key names to access the data.")
    exit()
except Exception as e:
    print(f"\nAn error occurred while loading or unpacking the file: {e}")
    exit()

# --- Step 3: Run the Test Prediction (same as before) ---
try:
    game_title_to_test = 'The Witcher 3: Wild Hunt'
    if game_title_to_test not in indices:
        print(f"\n'{game_title_to_test}' not found. Using the first game as a fallback.")
        game_title_to_test = df_clean['title'].iloc[0]

    print("-" * 40)
    print(f"Generating recommendations for: '{game_title_to_test}'")
    print("-" * 40)
    
    recommendations = get_content_based_recommendations(
        title=game_title_to_test, 
        cosine_sim=cosine_sim_matrix, 
        df=df_clean, 
        indices=indices, 
        n=10
    )

    if isinstance(recommendations, pd.Series):
        print("Top 10 Recommendations:")
        print(recommendations.to_string())
    else:
        print(recommendations)

except Exception as e:
    print(f"\nA critical error occurred during the recommendation process: {e}")

