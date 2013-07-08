## Warning: plugin still in alpha stage

# Sublime Text 2 plugin: RubyExtractMethod

Simply highlight a block of text and press the modifier keys to perform the extract method refactoring in a ruby file.

## Shortcut Keys

**Windows / OSX / Linux:**

 * `ALT+M` - Extract Method

#### How to perform the Extract Method refactoring in a Ruby file.
1. Select the block of code you wish to put into a method and hit the Shortcut Key
2. Name the method
3. Hit `Enter`
4. The method is now in your clipboard - so simply move your cursor to where you want to put the method, and hit `Ctrl+V` (or whatever your paste command is)

## Installation

### Git

``` bash
$ git clone git://github.com/pashamur/ruby-extract-method.git RubyExtractMethod
```

Further instructions below.

#### Windows XP, 7 and 8
Execute the commands below one by one in your Command prompt.

``` bash
$ cd "%APPDATA%\Sublime Text 2\Packages"
$ git clone git://github.com/pashamur/ruby-extract-method.git "RubyExtractMethod"
```

#### Linux
Execute the commands below one by one in your terminal.

``` bash
$ cd ~/.config/sublime-text-2/Packages/
$ git clone git://github.com/pashamur/ruby-extract-method.git RubyExtractMethod
```