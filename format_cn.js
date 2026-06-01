const fs = require('fs');
const path = require('path');

// Remove spaces between Chinese characters
function removeSpaceBetweenChinese(text) {
  let newText = text;
  while (/([\u4e00-\u9fa5])[ \t]+([\u4e00-\u9fa5])/.test(newText)) {
    newText = newText.replace(/([\u4e00-\u9fa5])[ \t]+([\u4e00-\u9fa5])/g, '$1$2');
  }
  return newText;
}

// Add spaces between Chinese and alphanumeric
function addSpaceBetweenChineseAndEnglish(text) {
  let newText = text;
  newText = newText.replace(/([\u4e00-\u9fa5])([a-zA-Z0-9])/g, '$1 $2');
  newText = newText.replace(/([a-zA-Z0-9])([\u4e00-\u9fa5])/g, '$1 $2');
  return newText;
}

function processText(text) {
  text = removeSpaceBetweenChinese(text);
  text = addSpaceBetweenChineseAndEnglish(text);
  return text;
}

// Process a Markdown file
function processFile(filePath) {
  if (!fs.existsSync(filePath)) return;
  let content = fs.readFileSync(filePath, 'utf8');
  const newContent = processText(content);
  if (content !== newContent) {
    fs.writeFileSync(filePath, newContent, 'utf8');
    console.log('Formatted:', filePath);
  }
}

// Process JSON file values
function processJsonFile(filePath) {
  if (!fs.existsSync(filePath)) return;
  let data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  
  function traverse(obj) {
    for (let key in obj) {
      if (typeof obj[key] === 'string') {
        if (!obj[key].startsWith('http')) {
          obj[key] = processText(obj[key]);
        }
      } else if (typeof obj[key] === 'object' && obj[key] !== null) {
        traverse(obj[key]);
      }
    }
  }
  
  traverse(data);
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
  console.log('Formatted:', filePath);
}

const mdFiles = ['ch/index.md'];
const dirs = ['_news', '_includes/intros', '_projects'];
dirs.forEach(d => {
  if (fs.existsSync(d)) {
    const files = fs.readdirSync(d).filter(f => f.endsWith('_zh.md'));
    files.forEach(f => mdFiles.push(path.join(d, f)));
  }
});

mdFiles.forEach(processFile);
processJsonFile('assets/json/resume_zh.json');
