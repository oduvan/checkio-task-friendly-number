"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "1. Base": [
        {
            "input": [102, {}],
            "answer": '102'
        },
        {
            "input": [12341234, {'decimals': 1}],
            "answer": '12.3M'
        },
        {
            "input": [102, {'decimals': 2}],
            "answer": '102.00'
        },
        {
            "input": [10240, {}],
            "answer": '10k'
        },
        {
            "input": [1024000000, {'base': 1024, 'suffix': 'iB'}],
            "answer": '976MiB'
        },
        {
            "input": [-150, {'base': 100, "powers": ['', 'd', 'D']}],
            "answer": '-1d'
        },
        {
            "input": [-155, {'base': 100, "decimals": 1, "powers": ['', 'd', 'D']}],
            "answer": '-1.6d'
        },
        {
            "input": [255000000000, {"powers": ['', 'k', 'M']}],
            "answer": '255000M'
        },



    ]
}
