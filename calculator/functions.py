

# Calculation
def Calculation(userChoice, operations_map, n1, n2, uuid, logger):
    if userChoice in operations_map:
        op_symbol, op_func = operations_map[userChoice]
        result = op_func(n1, n2)
        calculation = f"{n1} {op_symbol} {n2} = {result}"
        print(calculation)
        
        # Log with specific structured fields
        logger.info(
            calculation,
            extra={
                "operation": op_symbol,
                "operand1": n1,
                "operand2": n2,
                "result": result,
                "timestamp": datetime.now().isoformat(),
                "calculation_id": str(uuid.uuid4())
            }
        )
