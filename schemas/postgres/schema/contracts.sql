create table contracts
(
    address bytea,
    bytecode bytea,
    function_sighashes bytea[],
    is_erc20 bool,
    is_erc721 bool,
    block_number bigint
);