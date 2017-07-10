<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.


defined('MOODLE_INTERNAL') || die();
global $CFG, $PAGE;
%SKELETON_PREAMBLE%
class block_%BLOCKNAME_SHORT% extends block_base
{
    private static $blkName = '%BLOCKNAME_SHORT%';
    private $confDefault = array();

    public function __construct()
    {
        parent::__construct();
    }

    public function init()
    {
        $this->title = get_string(self::$blkName, 'block_'.self::$blkName);
    }

    public function get_content()
    {
        if ($this->content !== null) {
            // return $this->content; //FIXME: debug only
        }

        // set up default config values
		if (empty($this->config)) {
            $this->config = new stdClass();
            foreach ($this->confDefault as $k => $v) {
                $this->config->$k = $v;
            }
        }

        $this->content = new stdClass;

        $this->content->text = '';

        return $this->content;
    }
}
