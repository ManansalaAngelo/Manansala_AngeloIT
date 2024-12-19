@@ -0,0 +1,36 @@
def player(prev_play, opponent_history=[]):
    
    if prev_play:
        opponent_history.append(prev_play)
    # If no history, play "R" as a default first move
    if not opponent_history:
        return "R"
    # Strategy: Pattern Matching
    def find_pattern(history, length=3):
        if len(history) < length + 1:
            return None
        sequence = history[-length:]
        for i in range(len(history) - length):
            if history[i:i + length] == sequence:
                if i + length < len(history):
                    return history[i + length]
        return None
    pattern_length = 3
    predicted_move = find_pattern(opponent_history, pattern_length)
    if predicted_move:
        # Counter the predicted move
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        return counter_moves[predicted_move]
    # Fallback Strategy: Frequency Analysis (most common move of opponent)
    from collections import Counter
    move_counts = Counter(opponent_history)
    most_common_move = move_counts.most_common(1)[0][0] if move_counts else "R"
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[most_common_move]
