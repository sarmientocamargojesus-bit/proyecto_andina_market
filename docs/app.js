// Ruta RELATIVA: en un sitio de proyecto (usuario.github.io/proyecto_andina_market/)
// una ruta absoluta "/data/resumen.json" apuntaría a la raíz del dominio y daría 404.
const RUTA_RESUMEN = "data/resumen.json";

const soles = (n) => "S/ " + Number(n).toFixed(2);

function pintarTablero(r) {
  document.getElementById("total").textContent = soles(r.total_general);
  document.getElementById("operaciones").textContent = r.operaciones;
  document.getElementById("ticket").textContent = soles(r.ticket_promedio);

  const maximo = Math.max(...Object.values(r.total_por_sede));
  const grafico = document.getElementById("grafico");
  grafico.innerHTML = "";
  for (const [sede, total] of Object.entries(r.total_por_sede)) {
    const fila = document.createElement("div");
    fila.className = "fila";
    fila.innerHTML =
      `<span>${sede}</span>` +
      `<div class="pista"><div class="barra" style="width:${(total / maximo) * 100}%"></div></div>` +
      `<span class="monto">${soles(total)}</span>`;
    grafico.appendChild(fila);

    const tarjeta = document.getElementById(`sede-${sede}`);
    if (tarjeta) {
      tarjeta.querySelector(".valor").textContent = soles(total);
      tarjeta.querySelector(".detalle").textContent = `${r.operaciones_por_sede[sede]} operaciones`;
    }
  }
}

function pintarProductos(r) {
  const cuerpo = document.getElementById("productos");
  for (const [sede, productos] of Object.entries(r.productos_por_sede)) {
    const fila = document.createElement("tr");
    fila.innerHTML = `<th scope="row">${sede}</th><td>${productos.join(", ")}</td><td>${productos.length}</td>`;
    cuerpo.appendChild(fila);
  }
}

fetch(RUTA_RESUMEN)
  .then((res) => {
    if (!res.ok) throw new Error(`No se pudo leer ${RUTA_RESUMEN} (HTTP ${res.status})`);
    return res.json();
  })
  .then((r) => {
    if (document.getElementById("grafico")) pintarTablero(r);
    if (document.getElementById("productos")) pintarProductos(r);
  })
  .catch((error) => {
    document.getElementById("estado").textContent = error.message;
  });
