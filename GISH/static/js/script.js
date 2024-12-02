// Common variables
let scene, camera, renderer, textMesh;
let currentMaterial; // Store current material
let currentFontPath = '/static/fonts/MAGENTA.json'; // Default font path

// Initialize the scene
function init(containerId) {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x111111);

    camera = new THREE.PerspectiveCamera(10, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.set(0, 1, 20);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth / 2, window.innerHeight / 2);
    document.getElementById(containerId).appendChild(renderer.domElement);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0x404040, 2);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
    directionalLight.position.set(0, 1, 1).normalize();
    scene.add(directionalLight);

    // Set default material
    currentMaterial = new THREE.MeshStandardMaterial({
        color: 0xc57d5a, // Default: Rose Gold
        roughness: 0.5,
        metalness: 0.5,
    });

    // Load initial text
    loadFontAndCreateText("Gish");

    // Animate
    animate();
}

// Load font and create text
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
        size: 0.5,
        height: 0.1,
        curveSegments: 40,
        bevelEnabled: true,
        bevelThickness: 0.02,
        bevelSize: 0.01,
        bevelSegments: 5
    });

    if (textMesh) {
        scene.remove(textMesh);
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

// Update text dynamically
function updateText() {
    const userInput = document.getElementById('userInput').value.trim();
    if (userInput.length > 0 && userInput.length <= 10) {
        loadFontAndCreateText(userInput);
    } else {
        alert("Please enter a name with up to 10 characters.");
    }
}

// Update material dynamically
function updateMaterial(materialName) {
    switch (materialName) {
        case "Silver":
            currentMaterial = new THREE.MeshStandardMaterial({
                color: 0xc0c0c0, // Silver
                roughness: 0.5,
                metalness: 0.8,
            });
            break;
        case "Gold":
            currentMaterial = new THREE.MeshStandardMaterial({
                color: 0xffd700, // Gold
                roughness: 0.4,
                metalness: 0.9,
            });
            break;
        case "Rose Gold":
            currentMaterial = new THREE.MeshStandardMaterial({
                color: 0xc57d5a, // Rose Gold
                roughness: 0.5,
                metalness: 0.5,
            });
            break;
    }
    loadFontAndCreateText(document.getElementById('userInput').value || 'Gish');
}

// Update font dynamically
function updateFont(fontName) {
    switch (fontName) {
        case "Script":
            currentFontPath = '/static/fonts/MAGENTA.json';
            break;
        case "Bold":
            currentFontPath = '/static/fonts/block.json';
            break;
    }
    loadFontAndCreateText(document.getElementById('userInput').value || 'Gish');
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    if (textMesh) {
        textMesh.rotation.y += 0.003; // Rotate the text
    }
    renderer.render(scene, camera);
}

// Initialize the scene
if (document.getElementById('container')) {
    init('container');
}

// Handle window resizing
window.addEventListener('resize', function () {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});
