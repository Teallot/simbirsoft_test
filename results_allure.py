import allure_commons
from allure_commons.utils import now, uuid4
from allure_commons.reporter import AllureReporter
from allure_commons.logger import AllureFileLogger
from allure_commons.model2 import Status
from allure_commons.model2 import TestResult
from allure_commons.model2 import TestStepResult


def check(something):
    return something


if __name__ == '__main__':
    # Init allure
    allurelogdir = "results"
    logger = AllureReporter()
    file_logger = AllureFileLogger(allurelogdir)
    allure_commons.plugin_manager.register(file_logger)
    # Start testcase
    case_uuid = uuid4()
    testcase = TestResult(uuid=case_uuid, fullName='Test')
    logger.schedule_test(case_uuid, testcase)
    # TestStep
    allure_step = TestStepResult(name='step', start=now())
    current_step_uuid = uuid4()
    logger.start_step(None, current_step_uuid, allure_step)
    check('something')  # origial procedure for testing
    logger.stop_step(current_step_uuid, stop=now(), status=Status.PASSED)

    testcase.status = Status.PASSED
    logger.close_test(case_uuid)