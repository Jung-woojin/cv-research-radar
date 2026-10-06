import datetime as dt
import pathlib
import tempfile
import unittest
from radar_health import due, quality, report_path, scheduler_status


class HealthTests(unittest.TestCase):
    def test_weekdays_and_biweekly_anchor(self):
        job = {'days': [0], 'anchor': '2026-10-05', 'intervalDays': 14}
        self.assertTrue(due(job, dt.date(2026, 10, 5)))
        self.assertFalse(due(job, dt.date(2026, 10, 12)))
        self.assertTrue(due(job, dt.date(2026, 10, 19)))
        self.assertFalse(due({'days': [0, 1, 2, 3, 4]}, dt.date(2026, 10, 10)))

    def test_category_path_and_incomplete_report_detection(self):
        self.assertEqual(report_path({'path': 'daily/failures'}, dt.date(2026, 10, 7)),
                         'daily/failures/2026/10/2026-10-07.md')
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / 'report.md'
            self.assertEqual(quality(path), 'missing')
            path.write_text('# Radar\nGitHub archive fallback placeholder.\n')
            self.assertEqual(quality(path), 'placeholder')
            path.write_text('# Radar\nNo sources verified.\n')
            self.assertEqual(quality(path), 'needs_source_review')
            path.write_text('# Radar\nSource: https://example.org/paper\n')
            self.assertEqual(quality(path), 'present_needs_semantic_validation')
            path.write_text('status = "PAUSED"\n')
            self.assertEqual(scheduler_status(path), 'PAUSED')


if __name__ == '__main__':
    unittest.main()
