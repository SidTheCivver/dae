# Imports
import numpy
import pandas
rng = numpy.random.default_rng()
# Constants
AVAILABLE_STYLES = [
    "Country",
    "Jazz",
    "Blues",
    "Metal",
    "Prog"
]
LIST_OF_NOTES = [
    "A",
    "A#",
    "Bb",
    "B",
    "C",
    "C#",
    "Db",
    "D",
    "D#",
    "Eb",
    "E",
    "F",
    "F#",
    "Gb",
    "G",
    "G#",
    "Ab"
]
LIST_OF_CHORDS = [
    "A",
    "A#",
    "Bb",
    "B",
    "C",
    "C#",
    "Db",
    "D",
    "D#",
    "Eb",
    "E",
    "F",
    "F#",
    "Gb",
    "G",
    "G#",
    "Ab",
    "Am",
    "A#m",
    "Bbm",
    "Bm",
    "Cm",
    "C#m",
    "Dbm",
    "Dm",
    "D#m",
    "Ebm",
    "Em",
    "Fm",
    "F#m",
    "Gbm",
    "Gm",
    "G#m",
    "Abm"
]
RHYTHM_STYLE_DF = pandas.DataFrame({
    "Time Signature": [
        "4/4",
        "4/4",
        "4/4",
        "4/4",
        "2/4",
        "2/4",
        "4/4",
        "4/4",
        "4/4",
        "4/4",
        "4/4",
        "4/4",
        "4/4",
        "4/4",
        "7/8",
        "9/4",
        "4/4"
    ],
    "Rhythm": [
        "q q q q",
        "q e e q e e",
        "q e e re e e e",
        "e e e e e e e e",
        "e s s e s s",
        "s s e s s e",
        "q re q. q",
        "q re w",
        "q re e q re e",
        "q re e rq e re",
        "re q. q. e",
        "q q h",
        "q. q e",
        "e e e e e e e e",
        "q. q q",
        "w q w",
        "e e. e s e. e s e"
    ],
    "Available Styles": [
        ["Country"],
        ["Country"],
        ["Country"],
        ["Country", "Metal"],
        ["Metal"],
        ["Metal"],
        ["Metal"],
        ["Jazz"],
        ["Jazz"],
        ["Jazz"],
        ["Jazz"],
        ["Blues"],
        ["Blues"],
        ["Blues"],
        ["Prog"],
        ["Prog"],
        ["Prog"]
    ]
})
CHORD_PROGRESSION_DF = pandas.DataFrame({
    "Chord Progression": [
        (1, 4, 5, 1),
        (1, 5, 6, 4),
        (1, 4, 1, 5),
        (1, 6, 4, 5),
        (1, 5, 4, 1),
        (1, 6, 7),
        (1, 7, 6),
        (1, 6, 7, 1),
        (1, 7, 6, 7),
        (1, 2, 1),
        (1, 4, 5, 1),
        (2, 5, 1),
        (1, 6, 2, 5),
        (3, 6, 2, 5),
        (1, 4),
        (1, 4, 1, 1, 4, 4, 1, 1, 5, 4, 1, 5),
        (1, 4, 1, 5),
        (1, 4, 1, 5),
        (1, 7, 6, 1),
        (1, 4, 7, 3),
        (1, 3, 4, 2),
        (1, 6, 3, 7)
    ],
    "Major/Minor": [
        "Major",
        "Major",
        "Major",
        "Major",
        "Major",
        "Minor",
        "Minor",
        "Minor",
        "Minor",
        "Minor",
        "Major",
        "Major",
        "Major",
        "Major",
        "Major",
        "Major",
        "Major",
        "Minor",
        "Minor",
        "Minor",
        "Major",
        "Minor"
    ],
    "Style": [
        "Country",
        "Country",
        "Country",
        "Country",
        "Country",
        "Metal",
        "Metal",
        "Metal",
        "Metal",
        "Metal",
        "Jazz",
        "Jazz",
        "Jazz",
        "Jazz",
        "Jazz",
        "Blues",
        "Blues",
        "Blues",
        "Prog",
        "Prog",
        "Prog",
        "Prog"
    ]
})
SCALE_DF = pandas.DataFrame({
    "Major Key": [
        ["C"],
        ["C#", "Db"],
        ["D"],
        ["D#", "Eb"],
        ["E"],
        ["F"],
        ["F#", "Gb"],
        ["G"],
        ["G#", "Ab"],
        ["A"],
        ["A#", "Bb"],
        ["B"]
    ],
    "Minor Key": [
        ["Am"],
        ["A#m", "Bbm"],
        ["Bm"],
        ["Cm"],
        ["C#m", "Dbm"],
        ["Dm"],
        ["D#m", "Ebm"],
        ["Em"],
        ["Fm"],
        ["F#m", "Gbm"],
        ["Gm"],
        ["G#m", "Abm"],
    ],
    "Major Scale": [
        ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
        ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"],
        ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
        ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
        ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
        ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"],
        ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
        ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
        ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
        ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
        ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
        ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"]
    ],
    "Minor Scale": [
        ["Am", "Bdim", "C", "Dm", "Em", "F", "G"],
        ["Bbm", "Cdim", "Db", "Ebm", "Fm", "Gb", "Ab"],
        ["Bm", "C#dim", "D", "Em", "F#m", "G", "A"],
        ["Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb"],
        ["C#m", "D#dim", "E", "F#m", "G#m", "A", "B"],
        ["Dm", "Edim", "F", "Gm", "Am", "Bb", "C"],
        ["Ebm", "Fdim", "Gb", "Abm", "Bbm", "Cb", "Db"],
        ["Em", "F#dim", "G", "Am", "Bm", "C", "D"],
        ["Fm", "Gdim", "Ab", "Bbm", "Cm", "Db", "Eb"],
        ["F#m", "G#dim", "A", "Bm", "C#m", "D", "E"],
        ["Gm", "Adim", "Bb", "Cm", "Dm", "Eb", "F"],
        ["Abm", "Bbdim", "Cb", "Dbm", "Ebm", "Fb", "Gb"],
    ],
})


def main():
    print("Welcome to Sid Two's Chord Progression + Rhythm Generator")

    # Ask the user for style and key.
    style_prompt = "What style would you like? We have the following styles:"
    style_prompt = style_prompt + "\n 0: Random Style"
    for i in range(len(AVAILABLE_STYLES)):
        style_prompt = style_prompt + f"\n {i+1}: {AVAILABLE_STYLES[i]}"
    print(style_prompt)
    style_num = int(valid_input(
        prompt="Please select the number corresponding to the style "
        "you'd like",
        valid_inputs=[str(i) for i in range(1, len(AVAILABLE_STYLES)+1)],
        non_input="0"
    )
    )
    style = AVAILABLE_STYLES[style_num-1]
    key = valid_input(
        prompt="Select a key, or use N for a random one.",
        valid_inputs=LIST_OF_CHORDS,
        non_input="N"
    )

    # Select a rhythm and its corresponding time signature.
    available_rhythm_rows = RHYTHM_STYLE_DF[RHYTHM_STYLE_DF[
        "Available Styles"].apply(lambda x: style in x)]
    rhythm_row = available_rhythm_rows.sample().iloc[0]
    rhythm = str(rhythm_row["Rhythm"])
    time_sig = str(rhythm_row["Time Signature"])

    # Select a chord progression
    available_chord_progressions = CHORD_PROGRESSION_DF[
        CHORD_PROGRESSION_DF["Style"] == style
    ]
    chord_progression_row = available_chord_progressions.sample().iloc[0]

    # Find the chord scale row that corresponds to our key
    if "m" in key:
        scale_row = SCALE_DF[
            SCALE_DF["Minor Key"].apply(lambda x: key in x)].iloc[0]
    else:
        scale_row = SCALE_DF[
            SCALE_DF["Major Key"].apply(lambda x: key in x)].iloc[0]

    # Find out what scale we should be using.
    if str(chord_progression_row["Major/Minor"]) == "Major":
        scale = scale_row["Major Scale"]
    else:
        scale = scale_row["Minor Scale"]

    # Create a list of chords to play.
    chord_progression = chord_progression_row[
        "Chord Progression"
    ]
    chords = [scale[i-1] for i in chord_progression]

    user_key = ""

    if len(scale_row["Major Key"]) == 2:
        user_key += f"{scale_row["Major Key"][0]}/{scale_row["Major Key"][1]}"
    elif len(scale_row["Major Key"]) == 1:
        user_key += scale_row["Major Key"][0]
    user_key += " or "
    if len(scale_row["Minor Key"]) == 2:
        user_key += f"{scale_row["Minor Key"][0]}/{scale_row["Minor Key"][1]}"
    elif len(scale_row["Minor Key"]) == 1:
        user_key += scale_row["Minor Key"][0]

    # Give this information to the user
    print(f"Here is the selected key: {user_key}")
    print(f"Here is the selected style: {style}")
    print(f"Here is the rhythm: {rhythm}")
    print(f"Time signature: {time_sig}")
    print(f"Here is a list of the chords: {chords}")


def valid_input(prompt: str, valid_inputs: list[str],
                non_input: str = ""):
    """Asks for an input using the prompt, and checks if it is in the
    valid_inputs list. If it is non_input, then it picks a random value
    from the valid_inputs list."""
    print(prompt)
    is_valid = False
    user_input = valid_inputs[0]
    while is_valid is False:
        user_input = input("Answer: ")
        if user_input in valid_inputs:
            is_valid = True
        elif user_input == non_input:
            user_input = valid_inputs[rng.integers(len(valid_inputs))]
            is_valid = True
        else:
            print("Invalid input, please retry.")
    return user_input


if __name__ == "__main__":
    main()
