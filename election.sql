DROP TABLE IF EXISTS candidates;

CREATE TABLE candidates
(
    candidate_name VARCHAR(50) NOT NULL, 
    total_votes INT,
    PRIMARY KEY (candidate_name)
);

INSERT INTO candidates (candidate_name, total_votes)
VALUES
    ('Chairman Mao Tse Tung', 12),
    ('Donald J. Trump', 0),
    ('Madame Marie Curie', 567),
    ('Joy Division', 0)
;