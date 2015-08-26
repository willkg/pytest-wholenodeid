pytest-wholepath
================

pytest-wholepath will print the entire node id for test failures in the
header.

It turns this::

  =============================================== FAILURES ===============================================
  ______________________________ TriggerRuleMatchTests.test_match_locale _________________________________
  Traceback (most recent call last):
    File "/home/willkg/mozilla/fjord/fjord/suggest/providers/trigger/tests/test_models.py", line 24, in test_match_locale
      for tr_locales, feedback_locale, expected in tests:
  NameError: global name 'tests' is not defined

into this::

  =============================================== FAILURES ===============================================
  ____ fjord/suggest/providers/trigger/tests/test_models.py::TriggerRuleMatchTests::test_match_locale ____
  Traceback (most recent call last):
    File "/home/willkg/mozilla/fjord/fjord/suggest/providers/trigger/tests/test_models.py", line 24, in test_match_locale
      for tr_locales, feedback_locale, expected in tests:
  NameError: global name 'tests' is not defined

Why?

Because then you can copy and paste the node id in the header to more easily
run that specific test.


Quick start
===========

Install::

  $ pip install pytest-wholepath

It works by default. If you don't want wholepath, then you can pass
``--nowholepath`` as an argument to disable it.


Project details
===============

:Code:          https://github.com/willkg/pytest-wholepath
:Documentation: You're reading it
:Issue tracker: https://github.com/willkg/pytest-wholepath/issues
:License:       Simplified BSD License; see LICENSE file
