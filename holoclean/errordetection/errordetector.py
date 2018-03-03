from holoclean.errordetection.dcerrordetector import DCErrorDetection
from holoclean.errordetection.mysql_dcerrordetector import Mysql_DCErrorDetection

class ErrorDetectors:
    """
    This class call different error detection method that we needed
    """

    def __init__(self, DenialConstraints,
                 holo_obj,
                 dataset,
                 detection_type=None
                 ):
        """
        In this class we instantiate a DC error detector and pass dataengine to
        fill correspondence tables in data base
        :param DenialConstraints: list of denial constraints
        :param dataengine: list of dataengine
        :param spark_session: spark session
        :param dataset: dataset object for accessing tables name
        :param detection_type: type of errordetection
        """
        if detection_type is None:
            self.detect_obj = DCErrorDetection(DenialConstraints,
                                               holo_obj,
                                               dataset)
        elif detection_type == "mysql_DcErrorDetection":
            self.detect_obj = Mysql_DCErrorDetection (DenialConstraints,
                                               holo_obj,
                                               dataset)

    # Setters:

    # Getters:

    def get_noisy_dknow_dataframe(self, data_dataframe):

        """
        Return tuple of noisy cells and clean cells dataframes
        :param data_dataframe: get dataframe of data
        :return: return noisy cells and
        """

        noisy_cells = self.detect_obj.get_noisy_cells(data_dataframe)
        clean_cells = self.detect_obj.get_clean_cells(data_dataframe,
                                                      noisy_cells)

        return noisy_cells, clean_cells
