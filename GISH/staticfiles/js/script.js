// Global variables for Three.js
let scene, camera, renderer, textMesh;
let currentFontPath = '/static/fonts/MAGENTA.json'; // Default font
let currentMaterial = new THREE.MeshStandardMaterial({
    color: 0xc57d5a, // Default: Rose Gold
    roughness: 0.5,
    metalness: 0.5,
});

// Initialize the scene
function init(containerId) {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x111111);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 1, 4);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth / 2, window.innerHeight / 2);
    document.getElementById(containerId).appendChild(renderer.domElement);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0x404040, 2);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
    directionalLight.position.set(0, 1, 1).normalize();
    scene.add(directionalLight);

    // Load initial text
    loadFontAndCreateText('Gish');

    // Animation loop
    animate();
}

// Load font and create text mesh
function loadFontAndCreateText(message) {
    const fontLoader = new THREE.FontLoader();
    fontLoader.load(currentFontPath, function (font) {
        createTextMesh(message, font);
    });
}

// Create and add text mesh to the scene
function createTextMesh(message, font) {
    const textGeometry = new THREE.TextGeometry(message, {
        font: font,
        size: 1,
        height: 0.2,
        curveSegments: 12,
        bevelEnabled: true,
        bevelThickness: 0.05,
        bevelSize: 0.02,
        bevelSegments: 5,
    });

    if (textMesh) {
        scene.remove(textMesh); // Remove old text mesh
    }

    textMesh = new THREE.Mesh(textGeometry, currentMaterial);
    textGeometry.computeBoundingBox();
    const boundingBox = textGeometry.boundingBox;
    const center = new THREE.Vector3();
    boundingBox.getCenter(center);
    textGeometry.translate(-center.x, -center.y, -center.z);
    textMesh.position.set(0, 1, 0);
    scene.add(textMesh);
}

function updatePreview() {
    // Get the selected custom name
    const userInput = document.getElementById('id_custom_name').value.trim();

    // Get the selected font style
    const fontStyleElement = document.getElementById('id_font_style');
    const fontStyle = fontStyleElement.options[fontStyleElement.selectedIndex].text;

    // Get the selected material
    const materialElement = document.getElementById('id_material');
    const materialName = materialElement.options[materialElement.selectedIndex].text;

    // Update the font
    switch (fontStyle) {
        case 'Script':
            currentFontPath = '/static/fonts/MAGENTA.json';
            break;
        case 'Bold':
            currentFontPath = '/static/fonts/block.json';
            break;
        default:
            currentFontPath = '/static/fonts/MAGENTA.json'; // Default font
    }

    // Update the material
    switch (materialName) {
        case 'Silver':
            currentMaterial = new THREE.MeshStandardMaterial({
                color: 0xc0c0c0, // Silver
                roughness: 0.5,
                metalness: 0.8,
            });
            break;
        case 'Gold':
            currentMaterial = new THREE.MeshStandardMaterial({
                color: 0xffd700, // Gold
                roughness: 0.4,
                metalness: 0.9,
            });
            break;
        case 'Rose Gold':
            currentMaterial = new THREE.MeshStandardMaterial({
                color: 0xc57d5a, // Rose Gold
                roughness: 0.5,
                metalness: 0.5,
            });
            break;
        default:
            currentMaterial = new THREE.MeshStandardMaterial({
                color: 0xc57d5a, // Default: Rose Gold
                roughness: 0.5,
                metalness: 0.5,
            });
    }

    // Update the text
    if (userInput.length > 0 && userInput.length <= 10) {
        loadFontAndCreateText(userInput);
    } else {
        alert("Please enter a name with up to 10 characters.");
    }
}


// Animation loop
function animate() {
    requestAnimationFrame(animate);
    if (textMesh) {
        textMesh.rotation.y += 0.003; // Rotate the text
    }
    renderer.render(scene, camera);
}

// Initialize the scene on page load
if (document.getElementById('container')) {
    init('container');
}
