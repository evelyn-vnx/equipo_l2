# Art. 3 · Quality Standards (estándares de calidad)
- Backend: Laravel 10 php 8.3
    - Deberá seguir la guia de codificación PSR12
    - Deberá implementar tests unitarios para la capa de Dominio: Entities y ValueObjects
    - Deberá implementar tests de integración para la capa de Aplication: Use cases
    - Deberá trabajar con phpstan para validar sintaxis
    - Deberá usar pests 2.36 y mockey 1.4 para ejecutar tests
    - Carpeta legacy -> app/: MVC -> Services -> Repository
    - Carpeta DDD/Hexagonal src: UseCases, DTos inmutables entre cambas, CQS repositories
- Frontend: Nodejs 22 + Vue 3.4
    - Indentacion 2 espacios.
    - Naming camelCase
    - Sin punto y coma al final
    
# Art. 4 · Architecture Principles (principios de arquitectura)
- reglas de capas, patrones permitidos, anti-patrones prohibidos…
# Art. 7 · Boundaries (límites — las tres listas)
- ALWAYS DO: <…> · ASK FIRST: <…> · NEVER DO: <…>