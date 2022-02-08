import sentry_sdk
from sentry_sdk import capture_message


sentry_sdk.init(
    "https://25ccecc065054fafb511a8bd2c4ba068@o1095136.ingest.sentry.io/6114014",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    debug=True,
    environment = "walters_docker",
)

capture_message('Something went wrong')
#division_by_zero = 1 / 0