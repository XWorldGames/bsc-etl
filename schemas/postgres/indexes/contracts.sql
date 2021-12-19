alter table contracts add constraint contracts_pk primary key (address);

create index contracts_function_sighashes_index on contracts (function_sighashes);

create index contracts_is_erc20_index on contracts (is_erc20);
create index contracts_is_erc721_index on contracts (is_erc721);
create index contracts_block_number_index on contracts (block_number);
