// Common variables
let scene, camera, renderer, textMesh;

// Initialize the scene
function init(containerId) {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x111111);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 2, 5);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(600, 400);
    document.getElementById(containerId).appendChild(renderer.domElement);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0x404040, 2);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
    directionalLight.position.set(0, 1, 1).normalize();
    scene.add(directionalLight);

    // Initial text
    loadFontAndCreateText("GISH");

    // Animate
    animate();
}

// Load font and create text
function loadFontAndCreateText(message) {
    const fontLoader = new THREE.FontLoader();
    fontLoader.load('static/fonts/MAGENTA.json', function (font) {
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

    const textureLoader = new THREE.TextureLoader();
    const textMaterial = new THREE.MeshStandardMaterial({
        color: 0xffd700, // Gold color
        map: textureLoader.load('static/textures/text_texture.png')
    });

    if (textMesh) {
        scene.remove(textMesh);
    }

    textMesh = new THREE.Mesh(textGeometry, textMaterial);
    textGeometry.computeBoundingBox();
    const textWidth = textGeometry.boundingBox.max.x - textGeometry.boundingBox.min.x;
    textMesh.position.set(-textWidth / 2, 1, 0);
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

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    if (textMesh) {
        textMesh.rotation.y += 0.01; // Rotate the text
    }
    renderer.render(scene, camera);
}

// Initialize the scene
if (document.getElementById('container')) {
    init('container');
}

window.addEventListener('resize', function () {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});