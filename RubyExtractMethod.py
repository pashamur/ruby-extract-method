# Ruby Extract Method - Sublime Text 2 Plugin
# Created by Pasha Muravyev (pashamur)
# https://github.com/pashamur/ruby-extract-method

import sublime, sublime_plugin
import textwrap, string

class RubyExtractMethodCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.edit = edit
        self.view.window().show_input_panel("Please enter a name for the method: ", "", self.create_new_method, None, None)

    def create_new_method(self, method_name):
        selected_region = self.get_current_region()
        method_body = self.get_region_text(selected_region)

        self.replace_region_content_with_method_name(selected_region, method_name)

        new_method = self.build_new_method(method_name, method_body)
        sublime.set_clipboard(new_method)
        self.display_message("The method " + method_name + " is now in your clipboard. Use your keybinding for paste-with indent (default: Shift+Ctrl+V) to paste it into your code.")

    def get_current_region(self):
        regions = self.view.sel()
        return regions[0]

    def get_region_text(self, region):
        return self.view.substr(region)

    def replace_region_content_with_method_name(self, region, method_name):
        if self.region_ends_with_newline(region):
            self.view.replace(self.edit, region, method_name+"\n")
        else:
            self.view.replace(self.edit, region, method_name)
        self.view.window().run_command('reindent')

    def region_ends_with_newline(self, region):
        return (self.view.rowcol(region.end())[1] == 0)

    def build_new_method(self, method_name, method_body):
        new_method = "\ndef " + method_name + "\n"
        new_method += self.indent_text(method_body)
        new_method += "\nend\n"
        return new_method

    def indent_text(self, text):
        tab_size = self.view.settings().get('tab_size', 2)
        dedented_text = textwrap.dedent(string.expandtabs(text, tab_size))
        indented_text = "\n".join((tab_size * " ") + i for i in dedented_text.splitlines())
        return indented_text

    def display_message(self, value):
      sublime.active_window().active_view().set_status("ruby_extraction_msg", value)