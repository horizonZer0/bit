/**
 * Bit Converter
 * Converts values to 8-bit binary strings.
 */
export const Bit = (value) => {
    const str = String(value);
    return [...str]
        .map(char => char.charCodeAt(0).toString(2).padStart(8, '0'))
        .join(' ');
};
// At the bottom of index.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = Bit;
}
// Note: Do NOT define 'const Bit' again below this line. 
// If you need to use it, just call it: Bit("hello");