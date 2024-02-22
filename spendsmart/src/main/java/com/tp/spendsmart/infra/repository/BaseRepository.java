package com.tp.spendsmart.infra.repository;

import java.util.List;

/**
 * Base repository
 * @param <E> Entity type
 */
public interface BaseRepository<E> {

    /**
     * Find all entity data as list.
     * @return Data list
     */
    default List<E> findAll() {
        return List.of();
    }

}
