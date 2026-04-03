<?php

namespace horizonZer0\Bit;

class Converter 
{
    /**
     * Converts a value to 8-bit binary strings.
     * Works with Bit(123) or Bit($var) without quotes.
     */
    public static function Bit($value): string 
    {
        $text = (string)$value;
        $bits = [];
        
        for ($i = 0; $i < strlen($text); $i++) {
            $bits[] = str_pad(decbin(ord($text[$i])), 8, '0', STR_PAD_LEFT);
        }
        
        return implode(' ', $bits);
    }
}
