const units = {
  length: ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'],
  weight: ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces', 'tons'],
  temperature: ['celsius', 'fahrenheit', 'kelvin'],
  volume: ['liters', 'milliliters', 'gallons', 'quarts', 'cups', 'tablespoons', 'teaspoons'],
  area: ['square_meters', 'square_kilometers', 'square_feet', 'square_yards', 'acres', 'hectares'],
  speed: ['meters_per_second', 'kilometers_per_hour', 'miles_per_hour', 'feet_per_second', 'knots']
};

const unitLabels = {
  meters: 'Meters',
  kilometers: 'Kilometers',
  centimeters: 'Centimeters',
  millimeters: 'Millimeters',
  miles: 'Miles',
  yards: 'Yards',
  feet: 'Feet',
  inches: 'Inches',
  kilograms: 'Kilograms',
  grams: 'Grams',
  milligrams: 'Milligrams',
  pounds: 'Pounds',
  ounces: 'Ounces',
  tons: 'Tons',
  celsius: 'Celsius',
  fahrenheit: 'Fahrenheit',
  kelvin: 'Kelvin',
  liters: 'Liters',
  milliliters: 'Milliliters',
  gallons: 'Gallons',
  quarts: 'Quarts',
  cups: 'Cups',
  tablespoons: 'Tablespoons',
  teaspoons: 'Teaspoons',
  square_meters: 'Square Meters',
  square_kilometers: 'Square Kilometers',
  square_feet: 'Square Feet',
  square_yards: 'Square Yards',
  acres: 'Acres',
  hectares: 'Hectares',
  meters_per_second: 'Meters/Second',
  kilometers_per_hour: 'Kilometers/Hour',
  miles_per_hour: 'Miles/Hour',
  feet_per_second: 'Feet/Second',
  knots: 'Knots'
};

const conversionFactors = {
  length: {
    meters: 1.0,
    kilometers: 1000.0,
    centimeters: 0.01,
    millimeters: 0.001,
    miles: 1609.344,
    yards: 0.9144,
    feet: 0.3048,
    inches: 0.0254
  },
  weight: {
    kilograms: 1.0,
    grams: 0.001,
    milligrams: 0.000001,
    pounds: 0.453592,
    ounces: 0.0283495,
    tons: 1000.0
  },
  volume: {
    liters: 1.0,
    milliliters: 0.001,
    gallons: 3.78541,
    quarts: 0.946353,
    cups: 0.236588,
    tablespoons: 0.0147868,
    teaspoons: 0.00492892
  },
  area: {
    square_meters: 1.0,
    square_kilometers: 1000000.0,
    square_feet: 0.092903,
    square_yards: 0.836127,
    acres: 4046.86,
    hectares: 10000.0
  },
  speed: {
    meters_per_second: 1.0,
    kilometers_per_hour: 0.277778,
    miles_per_hour: 0.44704,
    feet_per_second: 0.3048,
    knots: 0.514444
  }
};

function convertTemperature(value, fromUnit, toUnit) {
  if (fromUnit === 'celsius') {
    if (toUnit === 'fahrenheit') return (value * 9/5) + 32;
    if (toUnit === 'kelvin') return value + 273.15;
    return value;
  } else if (fromUnit === 'fahrenheit') {
    if (toUnit === 'celsius') return (value - 32) * 5/9;
    if (toUnit === 'kelvin') return (value - 32) * 5/9 + 273.15;
    return value;
  } else if (fromUnit === 'kelvin') {
    if (toUnit === 'celsius') return value - 273.15;
    if (toUnit === 'fahrenheit') return (value - 273.15) * 9/5 + 32;
    return value;
  }
  return value;
}

function updateUnits() {
  const category = document.getElementById('category').value;
  const fromUnit = document.getElementById('from-unit');
  const toUnit = document.getElementById('to-unit');
  
  const categoryUnits = units[category];
  
  fromUnit.innerHTML = '';
  toUnit.innerHTML = '';
  
  categoryUnits.forEach((unit, index) => {
    fromUnit.innerHTML += `<option value="${unit}">${unitLabels[unit]}</option>`;
    toUnit.innerHTML += `<option value="${unit}">${unitLabels[unit]}</option>`;
  });
  
  if (categoryUnits.length > 1) {
    toUnit.selectedIndex = 1;
  }
  
  convert();
}

function convert() {
  const value = document.getElementById('value').value;
  const fromUnit = document.getElementById('from-unit').value;
  const toUnit = document.getElementById('to-unit').value;
  const category = document.getElementById('category').value;
  const resultDiv = document.getElementById('result');
  const formulaDiv = document.getElementById('formula');
  
  if (!value) {
    resultDiv.textContent = 'Enter a value to see the conversion';
    formulaDiv.textContent = '';
    return;
  }
  
  const numValue = parseFloat(value);
  let result;
  
  if (category === 'temperature') {
    result = convertTemperature(numValue, fromUnit, toUnit);
  } else {
    const factors = conversionFactors[category];
    const baseValue = numValue * factors[fromUnit];
    result = baseValue / factors[toUnit];
  }
  
  resultDiv.textContent = `${numValue} ${unitLabels[fromUnit]} = ${result.toFixed(6)} ${unitLabels[toUnit]}`;
  formulaDiv.textContent = `Conversion: ${fromUnit} -> ${toUnit}`;
}

document.addEventListener('DOMContentLoaded', function() {
  updateUnits();
});
