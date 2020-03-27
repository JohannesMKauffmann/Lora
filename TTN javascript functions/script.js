/*
	The device sends humidity and temperature data measured by a DHT11 sensor. The payload consists of two unsigned numbers
	with a single floating point precision. Those two nummbers are encoded as 3 bytes.
	
	The first byte represents the whole part of the humidity number and the second byte represents the whole part
	of the temperature data. The third byte is split into two parts. The four most significant bits, or four leftmost bits, represent
	the fractional part of the humidity data. The four least significant bits represent or the four rightmost bits, represent
	the fractional part of the temperature data.
*/


function Decoder(bytes, port) {
	var data = {};
	
	var hum_f = bytes[2] >> 4;				// shift 4 bits right, to get fractional part of humidity
	var temp_f = bytes[2] & 0x0F;			// destroy the leftmost part, to get fractional part of temperature
	
	var hum_string = bytes[0] + "." + hum_f.toString();
	var temp_string = bytes[1] + "." + temp_f.toString();
	
	data.humidity = parseFloat(hum_string);
	data.temperature = parseFloat(temp_string);
	
	return data;
}
