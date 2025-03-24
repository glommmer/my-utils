import time
import boto3
import logging


def get_list_from_athena(query: str, exclude_header: bool = True) -> list:
	athena = boto3.client("athena")
	start_query_execution_response = athena.start_query_execution(
		QueryString=query,
		WorkGroup="my_workgroup",
	)
	is_still_running = True
	while is_still_running:
		query_status = athena.get_query_execution(
			QueryExecutionId=start_query_execution_response["QueryExecutionId"]
		)["QueryExecution"]["Status"]
		if query_status["State"] == "SUCCEEDED":
			is_still_running = False
		elif query_status["State"] == "FAILED":
			reason = query_status["StateChangeReason"]
			raise RuntimeError(
				f"The Amazon Athena query failed to run with error message: {reason}"
			)
		elif query_status["State"] == "CANCELLED":
			raise RuntimeError("The Amazon Athena query was cancelled.")
		else:
			logging.info(f"The current status is: {query_status['State']}")
			time.sleep(1)
	paginator = athena.get_paginator("get_query_results")
	get_query_results_iterable = paginator.paginate(
		QueryExecutionId=start_query_execution_response["QueryExecutionId"]
	)
	temp_list = []
	for idx, result in enumerate(get_query_results_iterable):
		rows = result["ResultSet"]["Rows"]
		if exclude_header and idx == 0:
			rows = rows[1:]
		for row in rows:
			tmp_obj = tuple(r["VarCharValue"] for r in row["Data"])
			temp_list.append(tmp_obj)
	return temp_list