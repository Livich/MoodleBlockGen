# Moodle block generator

Skeleton generator for Moodle's blocks.

Usage:

`mbgen -n <your block name> -s <moodle internal block name> -d <destination directory> [-m <module list>]`

For example:

`mbgen -n "My Test Block" -s my_test_block -d "./test" -m libclass,skeleton"`

## Modules

There are some modules, which provides different features to your skeleton.

### `skeleton` module

Provides base skeleton structure. It creates:
 * Main block file
 * `./styles.css`
 * All `./db/` and `./lang/` stuff
 * `version.php`
 * `./lib/` directory to place your js, css, php, so on
 
 ### `libclass` module
 
Creates utility class for your block.