from heart_stroke.pipline.pipeline import Pipeline
from heart_stroke.config.configuration import Configuartion
from heart_stroke.constants import get_current_time_stamp

pipline=Pipeline(config=Configuartion(current_time_stamp=get_current_time_stamp()))
pipline.run_pipeline()