import { TableContainer, Table, TableHead, TableCell, TableBody, Paper, TableRow, Box, CircularProgress } from "@mui/material";



const SheduleTable = ({schedule, loading}) => {
  
    return (
      
        loading ?
        (<Box   sx={{ 
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh' 
        }}
        >
          <CircularProgress  size={80}/>
        </Box>)
              :
        (<TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>№</TableCell>
                <TableCell align="right">Назва</TableCell>
                <TableCell align="right">Виклачад</TableCell>
                <TableCell align="right">Аудиторія</TableCell>
                <TableCell align="right">Час</TableCell>
                
              </TableRow>
            </TableHead>
            
            <TableBody>
                    {schedule.map((item) =>
                       
                            <TableRow
                                key={item.id}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                 <TableCell component="th" scope="row">{item.number_subject}</TableCell>
                                <TableCell align="right">{item.subject.name}</TableCell>
                                <TableCell align="right">{`${item.subject.teacher.first_name} ${item.subject.teacher.last_name}`}</TableCell>
                                <TableCell align="right">{item.audience}</TableCell>
                                <TableCell align="right">{item.time}</TableCell>
                            </TableRow>
                    
                    )}
                </TableBody>
          
          </Table>
        </TableContainer>)
      );
}

export default SheduleTable;