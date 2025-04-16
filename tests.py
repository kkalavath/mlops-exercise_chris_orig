import os
import json
import app

def test_model_file_created():
    app.main()  # Assuming the main function encapsulates the training logic
    assert os.path.exists('models/model.pkl')

def test_model_score():
    print("Score:")
    score = app.main()  # Assuming the main function returns the score
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0
    print(score)
    # Load the model scores
    with open('model_scores.json', 'r') as f:
        model_scores = json.load(f)
    # Get the latest model score
    latest_score = model_scores[-1]['score'] 
    print("Latest_Score:", latest_score)
    # Compare the latest score with the current score
    assert score >= latest_score

    