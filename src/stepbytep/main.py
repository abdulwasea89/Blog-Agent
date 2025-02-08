#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crew import Stepbytep

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'LLM ',
        'current_year': datetime.now().year,
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }

    Stepbytep().crew().kickoff(inputs=inputs)

run()
