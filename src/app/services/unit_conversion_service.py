class UnitConversionService:
    def __init__(self):
        # Unit conversion factors (base unit = 1.0)
        self.conversion_factors = {
            'length': {
                'meters': 1.0,
                'kilometers': 1000.0,
                'centimeters': 0.01,
                'millimeters': 0.001,
                'miles': 1609.344,
                'yards': 0.9144,
                'feet': 0.3048,
                'inches': 0.0254
            },
            'weight': {
                'kilograms': 1.0,
                'grams': 0.001,
                'milligrams': 0.000001,
                'pounds': 0.453592,
                'ounces': 0.0283495,
                'tons': 1000.0
            },
            'volume': {
                'liters': 1.0,
                'milliliters': 0.001,
                'gallons': 3.78541,
                'quarts': 0.946353,
                'cups': 0.236588,
                'tablespoons': 0.0147868,
                'teaspoons': 0.00492892
            },
            'area': {
                'square_meters': 1.0,
                'square_kilometers': 1000000.0,
                'square_feet': 0.092903,
                'square_yards': 0.836127,
                'acres': 4046.86,
                'hectares': 10000.0
            },
            'speed': {
                'meters_per_second': 1.0,
                'kilometers_per_hour': 0.277778,
                'miles_per_hour': 0.44704,
                'feet_per_second': 0.3048,
                'knots': 0.514444
            }
        }
        
        self.available_units = {
            'length': ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'],
            'weight': ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces', 'tons'],
            'temperature': ['celsius', 'fahrenheit', 'kelvin'],
            'volume': ['liters', 'milliliters', 'gallons', 'quarts', 'cups', 'tablespoons', 'teaspoons'],
            'area': ['square_meters', 'square_kilometers', 'square_feet', 'square_yards', 'acres', 'hectares'],
            'speed': ['meters_per_second', 'kilometers_per_hour', 'miles_per_hour', 'feet_per_second', 'knots']
        }
    
    def convert_temperature(self, value, from_unit, to_unit):
        """Handle temperature conversions with special formulas"""
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return (value * 9/5) + 32
            elif to_unit == 'kelvin':
                return value + 273.15
            else:
                return value
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5/9
            elif to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
            else:
                return value
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
            else:
                return value
        else:
            return value
    
    def convert(self, value, from_unit, to_unit, category):
        """
        Convert a value from one unit to another within a category
        
        Args:
            value: The numeric value to convert
            from_unit: The unit to convert from
            to_unit: The unit to convert to
            category: The category of units (length, weight, temperature, etc.)
            
        Returns:
            dict: Conversion result with value, units, and result
            or dict with error key if conversion fails
        """
        # Validate inputs
        if category not in self.available_units:
            return {'error': f'Invalid category: {category}'}
        
        if from_unit not in self.available_units[category]:
            return {'error': f'Invalid from_unit: {from_unit} for category: {category}'}
        
        if to_unit not in self.available_units[category]:
            return {'error': f'Invalid to_unit: {to_unit} for category: {category}'}
        
        # Handle temperature conversions separately
        if category == 'temperature':
            result = self.convert_temperature(value, from_unit, to_unit)
        else:
            # Standard conversion using base unit
            factors = self.conversion_factors[category]
            
            # Convert to base unit, then to target unit
            base_value = value * factors[from_unit]
            result = base_value / factors[to_unit]
        
        return {
            'value': value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'category': category,
            'result': round(result, 6)
        }
    
    def get_available_units(self):
        """Get all available unit categories and their units"""
        return self.available_units
