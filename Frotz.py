import time
import subprocess
from os.path import exists, join, expanduser
import sys


class Frotz(object):
    def __init__(self, game_name,
                 interpreter,
                 save_file='save.qzl',
                 prompt_symbol=">",
                 reformat_spacing=True):
        self.data = game_name
        self.interpreter = interpreter
        self.save_file = save_file
        self.prompt_symbol = prompt_symbol
        self.reformat_spacing = reformat_spacing
        self.score = -1
        self.moves = -1
        self._get_frotz()

    def _get_frotz(self):
        print(self.data, self.interpreter)
        self.frotz = subprocess.Popen([self.interpreter, self.data],
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
        time.sleep(0.1)  # Allow to load

        # Load default savegame
        if exists(self.save_file):
            print('Loading saved game')
            self.restore(self.save_file)

    def save(self, filename=None):
        """
            Save game state.
        """
        sys.stderr.write("save() : Function not working!")
        return ""
        filename = filename or self.save_file
        self.do_command('save')
        time.sleep(0.5)
        self._clear_until_prompt(':')
        self.do_command(filename)  # Accept default savegame
        time.sleep(0.5)
        # Check if game returns Ok or query to overwrite
        while True:
            char = self.frotz.stdout.read(1)
            time.sleep(0.01)
            if char == b'.':  # Ok. (everything is done)
                break  # The save is complete
            if char == b'?':  # Indicates an overwrite query
                self.do_command('y')  # reply yes

        time.sleep(0.5)
        self._clear_until_prompt()

    def restore(self, filename=None):
        sys.stderr.write("restore() : Function not working!")
        return ""
        """
            Restore saved game.
        """
        filename = filename or self.save_file
        self.do_command('restore')
        time.sleep(0.5)
        self._clear_until_prompt(':')
        self.do_command(filename)  # Accept default savegame
        time.sleep(0.5)
        self._clear_until_prompt()

    def _clear_until_prompt(self, prompt=None):
        """ Clear all received characters until the standard prompt. """
        # Clear all data with title etcetera
        prompt = prompt or self.prompt_symbol
        char = self.frotz.stdout.read(1).decode()
        while char != prompt:
            time.sleep(0.001)
            char = self.frotz.stdout.read(1).decode()

    def do_command(self, action, parse_room=False):
        """ Write a command to the interpreter. """
        self.frotz.stdin.write(action.encode() + b'\n')
        self.frotz.stdin.flush()
        return self._frotz_read(parse_room)

    def _frotz_read(self, parse_room=False):
        """
            Read from frotz interpreter process.
            Returns tuple with Room name and description.
        """
        # Read room info
        output = ""
        output += self.frotz.stdout.read(1).decode()

        if not len(output):
            return ""
        while output[-1] != '>':
            output += self.frotz.stdout.read(1).decode('ISO-8859-1')
        # remove score lines if any
        lines = [l for l in output[:-1].split("\n") if l.strip() and "Score: " not in l]
        # make string with lines
        line = "\n".join(lines)
        if parse_room:
            room = lines[0]
            lines = lines[1:]
            line = "\n".join(lines)
            return room, line
        return line

    def get_intro(self, custom_parser=None):

        if custom_parser is not None:
            intro = custom_parser(self)
        else:
            output = ""
            saw_serial = False
            while not saw_serial:
                output += self.frotz.stdout.read(1).decode()
                while str(output)[-1] != '\n':
                    output += self.frotz.stdout.read(1).decode()
                    # print(output)
                if "serial number" in output.lower():
                    saw_serial = True
            intro = self._frotz_read(parse_room=False) + "\n"

        return intro.strip()

    def play_loop(self, parse_room=False):
        print(self.get_intro())
        user_quit = False
        try:
            while not self.game_ended() and not user_quit:
                user_input = input(">>")
                if parse_room:
                    room, description = self.do_command(user_input, parse_room)
                    print(room)
                    print(description)
                else:
                    output = self.do_command(user_input)
                    print(output)
                if user_input and user_input.lower() == "quit":
                    user_input = input(">>")
                    if user_input and user_input.lower() == "y":
                        self.do_command(user_input)
                        user_quit = True

        except KeyboardInterrupt:
            pass

    # toto: this needs to refine
    def game_ended(self):
        sys.stderr.write("game_ended() : Function not working!")
        return ""
        poll = self.frotz.poll()
        if poll is None:
            return False
        else:
            return True