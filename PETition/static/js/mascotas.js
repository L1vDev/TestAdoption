let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    responsive:true,
    columnDefs: [
        { searchable: false, targets: [0] }
    ],
    language: {
        decimal: "",
        emptyTable: "No hay información",
        info: "Mostrando _START_ a _END_ de _TOTAL_ Mascotas",
        infoEmpty: "No hay mascotas para mostrar",
        infoFiltered: "(Filtrado de _MAX_ total mascotas)",
        infoPostFix: "",
        thousands: ",",
        lengthMenu: "Mostrar _MENU_ Mascotas",
        loadingRecords: "Cargando...",
        processing: "Procesando...",
        search: "Buscar:",
        zeroRecords: "Sin resultados encontrados",
        paginate: {
            first: "Primero",
            last: "Ultimo",
            next: "Siguiente",
            previous: "Anterior"
        }
    },
        lengthMenu: [[1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 75, 100], [1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 75, 100]],
        pageLength: 5,
        destroy: true
    
};


const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    dataTable = $("#mascotas").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

window.addEventListener('load', async () => {
    await initDataTable();
});
