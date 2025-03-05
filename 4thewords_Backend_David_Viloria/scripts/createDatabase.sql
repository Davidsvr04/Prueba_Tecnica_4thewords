CREATE DATABASE 4thewords_prueba_david_viloria;
USE 4thewords_prueba_david_viloria;

CREATE TABLE leyendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha DATE NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    canton VARCHAR(255) NOT NULL,
    distrito VARCHAR(255) NOT NULL,
    imagen_url VARCHAR(255) NOT NULL
);

INSERT INTO leyendas (nombre, categoria, descripcion, fecha, provincia, canton, distrito, imagen_url)
VALUES
('La Llorona', 'Fantasmas', 'Una mujer que llora por sus hijos y aparece cerca de ríos y lagunas, causando terror con su lamento.', '1800-01-01', 'San José', 'Central', 'Catedral', 'https://citysites1.b-cdn.net/wp-content/uploads/sites/4/2021/02/35-1024x1024.webp'),
('El Cadejos', 'Criaturas', 'Un perro negro con ojos de fuego que protege a los borrachos de los peligros del camino.', '1700-01-01', 'Alajuela', 'Central', 'Alajuela', 'https://cdn.sanjosecostarica.org/wp-content/uploads/2020/07/El-Cadejo-485x485.jpg'),
('El Padre sin Cabeza', 'Fantasmas', 'Un sacerdote decapitado que aparece en los caminos oscuros de la ciudad.', '1825-01-01', 'Heredia', 'Heredia', 'Mercedes', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxhFaQpNMrvYN7YprX_FnKY9rkN2dwzi31MA&s'),
('La Tulevieja', 'Fantasmas', 'El espíritu de una mujer que perdió a su hijo y vaga en busca de él, asustando a quienes se cruzan con ella.', '1850-01-01', 'Cartago', 'Santa Cruz', 'Paraíso', 'https://tse3.mm.bing.net/th?id=OIP.8VqWMfbJ1dltn_ArpekvWAHaHa&pid=Api'),
('La Cegua', 'Criaturas', 'Una mujer que seduce a los hombres en el camino y se transforma en un monstruo aterrador.', '1775-01-01', 'Limón', 'Limón', 'Barrio Cieneguita', 'https://tse3.mm.bing.net/th?id=OIP.DSXL3rxpSeovquJDOuYTZAHaD4&pid=Api'),
('El Sombreron', 'Un hombre pequeño con un gran sombrero que encanta a las mujeres con su música y les impide dormir.', '1800-01-01', 'San José', 'Central', 'Carmen', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaNjOEqe0Gpl06X1hUvbBiUT37JsJ06DirZA&s');

