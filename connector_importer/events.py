# Author: Simone Orsi
# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.connector.event import Event

chunk_finished_event = Event()


@chunk_finished_event
def chunk_finished_subscriber(env, dest_model_name, last_record):
    """Run `import_record_after_all` after last record has been imported."""
    if not last_record.job_id:
        # ok... we are not running in cron mode..my job here has finished!
        return
    # TODO
    # backend = last_record.backend_id
    # recordset = last_record.recordset_id
    # other_records_completed = [
    #     r.job_id.state == 'done'
    #     for r in recordset.record_ids
    #     if r != last_record
    # ]
    # if all(other_records_completed):
    #     job_method = last_record.with_delay().import_record_after_all
    #     if backend.debug_mode():
    #         job_method = last_record.import_record_after_all
    #     job_method(last_record_id=record_id)
