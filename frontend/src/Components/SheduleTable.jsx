import { TableContainer, Table, TableHead, TableCell, TableBody, Paper, TableRow } from "@mui/material";



const SheduleTable = ({schedule}) => {
    console.log("Shedule:" + {schedule})
  
    return (
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Назва</TableCell>
                <TableCell align="right">Група</TableCell>
                {/* <TableCell align="right">День</TableCell> */}
                <TableCell align="right">Виклачад</TableCell>
                
              </TableRow>
            </TableHead>
            
            <TableBody>
                    {schedule.map((item) =>
                        item.subject.map((subject) => (
                            <TableRow
                                key={`${item.day}-${subject.name}`}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                <TableCell component="th" scope="row">{subject.name}</TableCell>
                                <TableCell align="right">{item.group.name}</TableCell>
                                {/* <TableCell align="right">{item.day}</TableCell> */}
                                <TableCell align="right">{`${subject.teacher.first_name} ${subject.teacher.last_name}`}</TableCell>
                            </TableRow>
                        ))
                    )}
                </TableBody>
          
          </Table>
        </TableContainer>
      );
}

export default SheduleTable;