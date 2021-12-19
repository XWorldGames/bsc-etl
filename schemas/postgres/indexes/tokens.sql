alter table tokens add constraint tokens_pk primary key (address);

create index tokens_is_erc721_index on tokens (is_erc721);
