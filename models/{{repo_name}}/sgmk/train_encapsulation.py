import os
import traceback
import sgmk.decorators.train


def train(input_data_path, model_save_path, input_config_file, hyperparams_path=None, failure_output=None):
    """
    The function to execute the training.
    :param input_config_file: input path to config json file.
    :param input_data_path: root input path
    :param model_save_path: [str], directory path to save your model(s)
    :param hyperparams_path: [optional[str], default=None], input path to hyperparams json file.
    Example:
        {
            "max_leaf_nodes": 10,
            "n_estimators": 200
        }
    :param failure_output: [optional[str], default=None], output directory path to save your
    failure(s) files
    """
    print('Training...')
    try:
        t = sgmk.decorators.train.train_function()
        t._function(input_data_path, model_save_path, input_config_file, hyperparams_path)
        # adjust_model_files_permissions(model_save_path)
        return True
    except Exception as e:
        # Write out an error file. This will be returned as the failureReason in the
        # DescribeTrainingJob result.
        trc = traceback.format_exc()
        if failure_output:
            # Printing this causes the exception to be in the training job logs, as well.
            print('Exception during training: ' + str(e) + '\n' + trc)
            with open(failure_output, 'w') as s:
                s.write('Exception during training: ' + str(e) + '\n' + trc)
            os.chmod(failure_output, 0o644)
        return False
        # A non-zero exit code causes the training job to be marked as Failed.
        # sys.exit(255)
