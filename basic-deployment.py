from prefect.deployments import DeploymentSpec, SubprocessFlowRunner

DeploymentSpec(
    name="basic-deployment",
    flow_location="./retry.py",
    flow_name="lambda-flow",
    parameters={"n": "3"},
    tags=["dog"],
    flow_runner=SubprocessFlowRunner()
)