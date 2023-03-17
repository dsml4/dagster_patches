from dagster import seven as __dm_seven
import dagstermill
import os


def load_params():
    params = {
        key: __dm_seven.json.loads(value)
        for key, value
        in {'executable_dict': '{"__class__": "ReconstructablePipeline", "asset_selection": null, "pipeline_name": "pipeline", "repository": {"__class__": "ReconstructableRepository", "container_context": null, "container_image": null, "entry_point": ["dagster"], "executable_path": "/usr/local/bin/python", "pointer": {"__class__": "FileCodePointer", "fn_name": "pipeline", "python_file": "/app/dag.py", "working_directory": "/app"}, "repository_load_data": null}, "solid_selection_str": null, "solids_to_execute": null}', 'pipeline_run_dict': '{"__class__": "PipelineRun", "asset_selection": null, "execution_plan_snapshot_id": "025717e9a406b5308260a4696962d17634913507", "external_pipeline_origin": {"__class__": "ExternalPipelineOrigin", "external_repository_origin": {"__class__": "ExternalRepositoryOrigin", "repository_location_origin": {"__class__": "ManagedGrpcPythonEnvRepositoryLocationOrigin", "loadable_target_origin": {"__class__": "LoadableTargetOrigin", "attribute": null, "executable_path": null, "module_name": null, "package_name": null, "python_file": "/app/dag.py", "working_directory": "/app"}, "location_name": "dag.py"}, "repository_name": "__repository__pipeline"}, "pipeline_name": "pipeline"}, "has_repository_load_data": false, "mode": "default", "parent_run_id": "7f379ef5-288c-4b73-89af-751553458e9a", "pipeline_code_origin": {"__class__": "PipelinePythonOrigin", "pipeline_name": "pipeline", "repository_origin": {"__class__": "RepositoryPythonOrigin", "code_pointer": {"__class__": "FileCodePointer", "fn_name": "pipeline", "python_file": "/app/dag.py", "working_directory": "/app"}, "container_context": {}, "container_image": null, "entry_point": ["dagster"], "executable_path": "/usr/local/bin/python"}}, "pipeline_name": "pipeline", "pipeline_snapshot_id": "73b87ac3f679baa3fefb0d504061875f3e6ef08a", "root_run_id": "7f379ef5-288c-4b73-89af-751553458e9a", "run_config": {}, "run_id": "92e67cd5-8e45-4227-92f3-b661c2b159bb", "solid_selection": null, "solids_to_execute": null, "status": {"__enum__": "PipelineRunStatus.STARTING"}, "step_keys_to_execute": ["nb_2"], "tags": {".dagster/grpc_info": "{\\"host\\": \\"localhost\\", \\"socket\\": \\"/tmp/tmp5edf_mfk\\"}", "dagster/parent_run_id": "7f379ef5-288c-4b73-89af-751553458e9a", "dagster/root_run_id": "7f379ef5-288c-4b73-89af-751553458e9a", "dagster/solid_selection": "*", "dagster/step_selection": "\\"nb_2\\""}}', 'node_handle_kwargs': '{"name": "nb_2", "parent": null}', 'instance_ref_dict': '{"__class__": "InstanceRef", "compute_logs_data": {"__class__": "ConfigurableClassData", "class_name": "LocalComputeLogManager", "config_yaml": "base_dir: /app/daghome/storage\\n", "module_name": "dagster.core.storage.local_compute_log_manager"}, "custom_instance_class_data": null, "event_storage_data": {"__class__": "ConfigurableClassData", "class_name": "SqliteEventLogStorage", "config_yaml": "base_dir: /app/daghome/history/runs/\\n", "module_name": "dagster.core.storage.event_log"}, "local_artifact_storage_data": {"__class__": "ConfigurableClassData", "class_name": "LocalArtifactStorage", "config_yaml": "base_dir: /app/daghome\\n", "module_name": "dagster.core.storage.root"}, "run_coordinator_data": {"__class__": "ConfigurableClassData", "class_name": "DefaultRunCoordinator", "config_yaml": "{}\\n", "module_name": "dagster.core.run_coordinator"}, "run_launcher_data": {"__class__": "ConfigurableClassData", "class_name": "DefaultRunLauncher", "config_yaml": "{}\\n", "module_name": "dagster"}, "run_storage_data": {"__class__": "ConfigurableClassData", "class_name": "SqliteRunStorage", "config_yaml": "base_dir: /app/daghome/history/\\n", "module_name": "dagster.core.storage.runs"}, "schedule_storage_data": {"__class__": "ConfigurableClassData", "class_name": "SqliteScheduleStorage", "config_yaml": "base_dir: /app/daghome/schedules\\n", "module_name": "dagster.core.storage.schedules"}, "scheduler_data": {"__class__": "ConfigurableClassData", "class_name": "DagsterDaemonScheduler", "config_yaml": "{}\\n", "module_name": "dagster.core.scheduler"}, "secrets_loader_data": null, "settings": {}, "storage_data": {"__class__": "ConfigurableClassData", "class_name": "DagsterSqliteStorage", "config_yaml": "base_dir: /app/daghome\\n", "module_name": "dagster.core.storage.sqlite_storage"}}', 'step_key': '"nb_2"', 'output_log_path': '"/tmp/tmpxpahsls_"', 'marshal_dir': '"/tmp/dagstermill/92e67cd5-8e45-4227-92f3-b661c2b159bb/marshal"', 'run_config': '{}'}.items()
    }
    return params


def reconstitute_pipeline_contex(params):
    context = dagstermill._reconstitute_pipeline_context(**params)
    return context


if __name__ == '__main__':
    params = load_params()
    os.chdir(params['executable_dict']['repository']['pointer']['working_directory'])
    print(os.getcwd())
    context = reconstitute_pipeline_contex(params)
    url_nb_1_data1 = dagstermill._load_input_parameter('url_nb_1_data1')
    print(url_nb_1_data1)
