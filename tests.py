import os
import app
import json
import os


def test_model_file_created():
    app.main()  # Assuming the main function encapsulates the training logic
    assert os.path.exists('models/model.pkl')

def test_model_score():
    import os
    
    score = app.main()  # Assuming the main function returns the score
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0

    # Initialize model_scores
    if os.path.exists('model_scores.json') and os.path.getsize('model_scores.json') > 0:
        # Load existing model scores
        with open('model_scores.json', 'r') as f:
            model_scores = json.load(f)
            
        # Check if model_scores has any entries
        if model_scores:  # This checks if the list is not empty
            # Get the latest model version and increment it
            latest_version = float(model_scores[-1]['version'])
            new_version = f"{latest_version + 0.1:.1f}"
            
            # Get the latest score for comparison
            latest_score = model_scores[-1]['score']
            
            # Compare the latest score with the current score
            assert score >= latest_score
        else:
            # If the list is empty, initialize with first entry
            new_version = "1.0"
    else:
        # If file doesn't exist or is empty, initialize with first entry
        model_scores = []
        new_version = "1.0"
    
    # Add the new score entry
    model_scores.append({
        "version": new_version,
        "score": score
    })
    
    # Write updated scores back to file
    with open('model_scores.json', 'w') as f:
        json.dump(model_scores, f, indent=4)