"""
Unit tests for reading objects from a stream.
"""

import io
import unittest
from PyPDF2 import generic, utils


def make_stream(s):
    """Converts a string into a test input stream."""
    b = utils.b_(s)
    return io.BytesIO(b)


class Null(unittest.TestCase):
    """Tests for reading a NullObject."""
    def test_type(self):
        """Confirm the correct object type is created."""
        s = make_stream('null')
        o = generic.NullObject.readFromStream(s)
        self.assertIsInstance(o, generic.NullObject)

    def test_length(self):
        """Confirm the correct number of bytes are read from the input."""
        s = make_stream('null')
        generic.NullObject.readFromStream(s)
        pos = s.tell()
        self.assertEqual(pos, 4)

    def test_eof(self):
        """Confirm an exception is raised if an EOF occurs in the input."""
        s = make_stream('nul')
        with self.assertRaises(utils.PdfReadError):
            generic.NullObject.readFromStream(s)

    def test_invalid_keyword(self):
        """Confirm an exception is raised given an incorrect keyword."""
        s = make_stream('NULL')
        with self.assertRaises(utils.PdfReadError):
            generic.NullObject.readFromStream(s)


class Boolean(unittest.TestCase):
    """Tests for reading a Boolean object."""
    def test_type(self):
        """Confirm the correct object type is created."""
        s = make_stream('true')
        o = generic.BooleanObject.readFromStream(s)
        self.assertIsInstance(o, generic.BooleanObject)

    def test_true_value(self):
        """Confirm a true value is recorded as a True boolean object."""
        s = make_stream('true')
        o = generic.BooleanObject.readFromStream(s)
        self.assertIs(o.value, True)

    def test_false_value(self):
        """Confirm a false value is recorded as a False boolean object."""
        s = make_stream('false')
        o = generic.BooleanObject.readFromStream(s)
        self.assertIs(o.value, False)

    def test_true_length(self):
        """Confirm 4 bytes are read for a true value."""
        s = make_stream('true')
        generic.BooleanObject.readFromStream(s)
        pos = s.tell()
        self.assertEqual(pos, 4)

    def test_false_length(self):
        """Confirm 5 bytes are read for a false value."""
        s = make_stream('false')
        generic.BooleanObject.readFromStream(s)
        pos = s.tell()
        self.assertEqual(pos, 5)

    def test_eof(self):
        """Confirm an exception is raised if an EOF occurs in the input."""
        s = make_stream('tru')
        with self.assertRaises(utils.PdfReadError):
            generic.BooleanObject.readFromStream(s)

    def test_invalid_keyword(self):
        """Confirm an exception is raised given an incorrect keyword."""
        s = make_stream('TRUE')
        with self.assertRaises(utils.PdfReadError):
            generic.BooleanObject.readFromStream(s)
