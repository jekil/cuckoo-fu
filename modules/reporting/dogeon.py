# Copyright (C) 2014 Alessandro Tanasi - @jekil.
# This file is licensed with the same license of Cuckoo Sandbox - http://www.cuckoosandbox.org

# HOW TO INSTALL:
#
# Setup requirements with:
# pip install dogeon
#
# Copy this file in reporting modules folder, in /modules/reporting. Enable the module
# Adding the following lines to reporting.conf, in /conf/reporting.conf:
#
# [dogeon]
# enabled = yes
#
# Run cuckoo and use doge power with care.

import os
import dson
import codecs

from lib.cuckoo.common.abstracts import Report
from lib.cuckoo.common.exceptions import CuckooReportError

class DogeonDump(Report):
    """Saves analysis results in Dogeon format."""

    def run(self, results):
        """Writes report.
        @param results: Cuckoo results dict.
        @raise CuckooReportError: if fails to write report.
        """
        try:
            path = os.path.join(self.reports_path, "report.doge")
            report = codecs.open(path, "w", "utf-8")
            dson.dump(results, report, indent=4)
            report.close()
        except (UnicodeError, TypeError, IOError) as e:
            raise CuckooReportError("Failed to generate Dogeon report: %s" % e)
