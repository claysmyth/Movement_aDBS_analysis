import numpy as np
import pandas as pd
import utils

allowed_levels = ['zero', 'low', 'high']
allowed_assessments = ['UPDRS', 'ADL']
allowed_med_states = ['ON', 'OFF']
allowed_sides = ['left', 'right']


class ClinicSession:

    def __init__(self, session_file_path, stim_log, med_state, hemisphere, stim_level, assessment):
        self.rcs_df = utils.import_data(session_file_path)
        self.stim_df = utils.import_data(stim_log)

        self.med_state = med_state
        if not any(x in self.med_state for x in allowed_med_states):
            raise ValueError

        self.side = hemisphere
        if not any(x in self.side for x in allowed_sides):
            raise ValueError

        self.stim_level = stim_level
        if not any(x in self.stim_level for x in allowed_levels):
            raise ValueError

        self.assessment = assessment
        if not any(x in self.assessment for x in allowed_assessments):
            raise ValueError
