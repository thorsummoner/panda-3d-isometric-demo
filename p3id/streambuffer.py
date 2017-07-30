""" https://stackoverflow.com/a/29834357
"""
import os
import sys
import threading
import time

BLACKLIST_OS_NAMES = [
    'nt',
]


class StreamBuffer(object):
    """ Class used to grab standard output or another stream.
    """
    escape_char = b"\b"
    stream_fd = None
    worker_thread = None

    def __init__(self, stream=None, threaded=False):
        self.target_stream = stream
        self.threaded = threaded
        if self.target_stream is None:
            self.target_stream = sys.stdout

        self.target_stream_fd = self.target_stream.fileno()
        self.captured_text = bytearray()
        # Create a pipe so the stream can be captured:
        self.pipe_out, self.pipe_in = os.pipe()


    def __enter__(self):
        """ Start capturing the stream data.
        """
        self.captured_text = bytearray()
        # Save a copy of the stream:
        self.stream_fd = os.dup(self.target_stream_fd)
        # Replace the Original stream with our write pipe
        os.dup2(self.pipe_in, self.target_stream_fd)
        if self.threaded:
            # Start thread that will read the stream:
            self.worker_thread = threading.Thread(target=self._read_output)
            self.worker_thread.start()
            # Make sure that the thread is running and os.read is executed:
            time.sleep(0.01)


    def __exit__(self, exc_type, exc_value, exc_tb):
        """ Stop capturing the stream data and save the text in `captured_text`.
        """
        # Print the escape character to make the _read_output method stop:
        self.target_stream.write(self.escape_char.decode('ascii'))
        # Flush the stream to make sure all our data goes in before
        # the escape character.
        self.target_stream.flush()
        if self.threaded:
            # wait until the thread finishes so we are sure that
            # we have until the last character:
            self.worker_thread.join()
        else:
            self._read_output()
        # Close the pipe:
        os.close(self.pipe_out)
        # Restore the original stream:
        os.dup2(self.stream_fd, self.target_stream_fd)


    def _read_output(self):
        """
        Read the stream data (one byte at a time)
        and save the text in `captured_text`.
        """
        while True:
            data = os.read(self.pipe_out, 1)  # Read One Byte Only
            if self.escape_char in data:
                break
            if not data:
                break
            self.captured_text += data

if os.name in BLACKLIST_OS_NAMES:
    class StreamBuffer:
        """ Tulio: The stars are not in position for this tribute!
            Miguel: Like he said! Stars!... Can't do it... Not today.

            >+;r)/;(|")rrr/==r*"|"|;|;r)=;"=r*|"|r/r;r);)*"*r?r|"/rrr?"=;=";;r=?r
            <;r=;*r=r\/=|"r=;"|"r;"\"=\=(?*;;rrrr"*")=?=*r;;;r*|;r=**;=";==r*\)*r
            aeeI21i|;=r"|?()""r;r;;=*==**rr*;"\*r";;?;*|=)**;r;;;r";=*"=r"||=;"//
            HWQggRQ@PtL/"r\(|(\=;r(;=)**;"r)|r;*r|(|;r(/r")/=?;""***"|\/*rr;";;))
            @@RRRQgHgWNM$Jyx|*|r*;\(*|?=*);;=;"=;;"=*==;;*;r/\v}Yy4$S6mqP$yv?;*|*
            noV6b&QgQWHRBHNj+r**"";*(cYv*=;=**\)\vi[Yfuak9dM&&gWWHWRQHQRBBB@Es/"=
            6J2SMBMe2w&HQWWd|r="==;>\$DDOMOOMM@@@RHQRQRRBWQQWHWQBHRBWHWQgQRWgBDX{
            RhTe6?_ -`>nBWWRe"=";;r>+l&WBRBBBHRHRHHgWBQRQWRW@@@MKA9ZX5kV43aZbD@gH
            k4t1;'.- .)p@gBBHV|;r*rr;"7hgRWWQWQHBBQHQNMOqKdbh%%hZk3F2oIJuFoo3j#5p
            y1Tc_``  `?ORBBQHW4|"=((=";/z9G0MOp8hPXVakbO@DMP54a3aPMOA3CFnununC#eI
            siix|'  .`-;ZOgHRRZvrr*("?}zFnuoCCjjnj4MDOIi+!--  .<"=||JMMkftonCFuFV
            ivivii_ ---'-!r(v7i|\\)/)(}ztssztztFose$T_`.   '!YIMWgROCi5NE11Tfsz22
            "=;/???v/"+!_ ' ,//||"";?|l1Y1Y1YTYzysC>   `'-.>6NNHHHgRgG=ANe}YzTyzt
            =r";))???|/i?*?xYTv"*r"="\cxTlT1cTYYYYY.'''' '';OBHWHQQQQM^rPM]}YTlT1
            ===="=\\|/(??/\}1v\"*rr*)|(viivL7[c1YTY^       `)A&gRgQN8v.`TDci}{c7}
            =;=""*;;r"|=*|)YT"=**|**;)(\\?\|iiii{7T;.  --' ``.+ixYv;.`,+]Yvvxivic
            ;"*r="rrr"*=r"ici;*=r;=;=="|??(|))iiiiiLv*+!!~:~!:,<>"==??vvvi/vvvviv
            "?())?\;*|*="\Lc)"r"*;r;=r*"(/)/\=\?/\|/|viivvvivviviii(\\i)/?\|/\/|\
            ;"*|"r";r;="?vxv*;r;;r*=;";(r(r=*r"rr;;)?((?||||\|?(/\)r)||;?/r\="***
            r;*(|/|/\=""\{ir;="/;"";""r|/?"\=r()**r=|"*;=*=";**\r";;;;""=;"";|=";
        """
        def __init__(self, stream=None, threaded=False):
            pass

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_value, exc_tb):
            pass
